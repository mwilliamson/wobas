from nose.tools import istest, assert_equal
import funk

from wobas import buckets, injection


@istest
def bucket_is_same_as_corprus_if_corprus_has_the_same_number_of_words():
    source_string = "one two three"
    bucket_generator = injection.get(buckets.BucketGenerator)
    bucket = bucket_generator.generate_bucket_from_source_string(source_string, size=3)
    assert_equal({"one": 1, "two": 1, "three": 1}, bucket)


@istest
@funk.with_context
def bucket_is_generated_using_random_selection_from_source(context):
    source_string = "one two three"
    
    random = context.mock()
    funk.allows(random).sample(["one", "two", "three"], 2).returns(["one", "three"])
    
    bucket_generator = buckets.BucketGenerator(random=random)
    bucket = bucket_generator.generate_bucket_from_source_string(source_string, size=2)
    assert_equal({"one": 1, "three": 1}, bucket)


@istest
@funk.with_context
def bucket_can_have_same_word_multiple_times(context):
    source_string = "one two two"
    
    random = context.mock()
    funk.allows(random).sample(["one", "two", "two"], 2).returns(["two", "two"])
    
    bucket_generator = buckets.BucketGenerator(random=random)
    bucket = bucket_generator.generate_bucket_from_source_string(source_string, size=2)
    assert_equal({"two": 2}, bucket)
