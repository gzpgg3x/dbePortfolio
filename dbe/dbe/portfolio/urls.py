# from django.conf.urls.defaults import *
from django.conf.urls import *
from dbe.portfolio.models import *
from dbe.portfolio.views import *

urlpatterns = patterns("dbe.portfolio.views",
   (r"^group/(?P<dpk>\d+)/(?P<show>\S+)/" , GroupView.as_view(), {}, "group"),
   (r"^group/(?P<dpk>\d+)/"               , GroupView.as_view(), {}, "group"),
   (r"^add-images/(?P<dpk>\d+)/"          , AddImages.as_view(), {}, "add_images"),
   (r"^slideshow/(?P<dpk>\d+)/"           , SlideshowView.as_view(), {}, "slideshow"),
   (r"^image/(?P<mfpk>\d+)/"              , ImageView.as_view(), {}, "image"),
   (r"^image/"                            , ImageView.as_view(), {}, "image"),
   (r""                                   , Main.as_view(), {}, "portfolio"),
)
