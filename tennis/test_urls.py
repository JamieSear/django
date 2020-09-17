from . import urls
import pytest

def test_paths():
    # urls.urlpatterns()
    assert len(urls.urlpatterns) == 3