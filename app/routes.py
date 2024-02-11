from rest_framework.routers  import DefaultRouter
from app.views.Authorviews import AuthorViewSet
from app.views.Bookviews import BookViewSet

router = DefaultRouter()

router.register("book", BookViewSet)
router.register("author", AuthorViewSet)