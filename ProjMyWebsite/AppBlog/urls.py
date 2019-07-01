# -*- coding: utf-8 -*-

from django.conf.urls import url
from AppBlog import views

app_name = 'blog'

urlpatterns = [url(r'^$', views.PostListView.as_view(), name='postmodel_list'),
               url(r'^about/$', views.AboutView.as_view(), name='about'),
               url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(),
                   name='postmodel_detail'),
               url(r'^post/new/$', views.CreatePostView.as_view(),
                   name='postmodel_new'),
               url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(),
                   name='postmodel_edit'),
               url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(),
                   name='postmodel_remove'),
               url(r'^drafts/$', views.DraftListView.as_view(),
                   name='postmodel_draft_list'),
               url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post,
                   name='add_comment_to_postmodel'),
               url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve,
                   name='comment_approve'),
               url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove,
                   name='comment_remove'),
               url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish,
                   name='postmodel_publish'),
                   ]
