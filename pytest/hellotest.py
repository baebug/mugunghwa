import pytest
from blog.models import Post

@pytest.fixture
def first():
    print("Set up first fixture")
    yield
    print("Clean up first fixture")


@pytest.fixture
def second(first):
    print("Set up second fixture")
    yield
    print("Clean up second fixture")


def test_context_fixture_order(second):
    print("In the test")
    assert True
    

@pytest.fixture
def setup_post():
    Post.objects.create(title="test_title1", text="test_text1")
    print("Set up second fixture")
    yield
    print("Clean up second fixture")

@pytest.mark.django_db
def test_post(setup_post):
    test1 = Post.objects.get(title="test_title1")
    print(test1)
    assert test1.text == "test_text1"
    assert Post.objects.all().count() == 1