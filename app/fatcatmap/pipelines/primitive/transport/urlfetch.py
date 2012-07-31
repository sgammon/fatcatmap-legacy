# -*- coding: utf-8 -*-
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
from fatcatmap.models.transport import urlfetch as models
from fatcatmap.pipelines.primitive.transport import TransportPipeline


## URLFetchPipeline - parent to all URLFetch-based pipelines
class URLFetchPipeline(TransportPipeline):

    ''' Abstract parent class for low-level URL fetch pipelines. '''

    api = urlfetch


## FetchURL - fetches a URL and yields the result directly
class FetchURL(URLFetchPipeline):

    ''' Retrieve a URL and yield a structure with the status code, result content, final URL and response headers directly. '''

    def run(self, url, payload=None, method='GET', headers={}, allow_truncated=False, follow_redirects=True, deadline=None, validate_certificate=None):

        if 'http' not in url and 'https' not in url:
            try:
                key = ndb.Key(urlsafe=url)
            except:
                pass
            else:
                operation = key.get()
                url, payload, method, headers,
                allow_truncated, follow_redirects,
                deadline, validate_certificate =  operation.url, operation.payload, operation.method, operation.headers, operation.allow_truncated, operation.follow_redirects, operation.deadline, operation.validate_certificate

        else:
            operation = models.FetchOperation(**{
                'url': url,
                'payload': payload,
                'method': method,
                'headers': headers,
                'allow_truncated': allow_truncated,
                'follow_redirects': follow_redirects,
                'deadline': deadline,
                'validate_certificate': validate_certificate
            })
            okey = operation.put()

        if headers is None:
            headers = {}

        try:
            operation.status = 'fetching'
            operation.put()
            f = self.api.fetch(url, payload, method, headers, allow_truncated, follow_redirects, deadline, validate_certificate)

        except self.api.InvalidURLError, e:
            operation.status = 'error'
            operation.put()
            return {'status': 'failure', 'operation': operation.key.urlsafe(), 'error': {'exception': 'InvalidURLError', 'message': str(e)}}

        except self.api.DownloadError, e:
            operation.status = 'error'
            operation.put()
            return {'status': 'failure', 'operation': operation.key.urlsafe(), 'error': {'exception': 'DownloadError', 'message': str(e)}}

        except self.api.ResponseTooLargeError, e:
            operation.status = 'error'
            operation.put()
            return {'status': 'failure', 'operation': operation.key.urlsafe(), 'error': {'exception': 'ResponseTooLargeError', 'message': str(e)}}

        else:
            operation.status = 'success'
            operation.put()
            return {'status': 'success', 'operation': operation.key.urlsafe(), 'result': {'status_code': f.status_code, 'content': f.content, 'truncated': f.content_was_truncated, 'headers': f.headers, 'final_url': f.final_url}}


## DownloadURL - fetches a URL and yields a *reference* to the result
class DownloadURL(URLFetchPipeline):

    ''' Retrieve a URL and yield a *reference* to a persisted structure with the status code, result content, final URL and response headers. '''

    def run(self, url, payload=None, method='GET', headers={}, allow_truncated=False, follow_redirects=True, deadline=None, validate_certificate=None):

        if 'http' not in url and 'https' not in url:
            try:
                okey = ndb.Key(urlsafe=url)
            except:
                pass
            else:
                operation = okey.get()
                url, payload, method, headers,
                allow_truncated, follow_redirects,
                deadline, validate_certificate = operation.url, operation.payload, operation.method, operation.headers, operation.allow_truncated, operation.follow_redirects, operation.deadline, operation.validate_certificate

        else:
            operation = models.FetchOperation(**{
                'url': url,
                'payload': payload,
                'method': method,
                'headers': headers,
                'allow_truncated': allow_truncated,
                'follow_redirects': follow_redirects,
                'deadline': deadline,
                'validate_certificate': validate_certificate
            })
            okey = operation.put()

        if headers is None:
            headers = {}

        try:
            operation.status = 'fetching'
            operation.put()
            f = self.api.fetch(url, payload, method, headers, allow_truncated, follow_redirects, deadline, validate_certificate)

        except self.api.InvalidURLError, e:
            operation.status = 'error'
            operation.put()
            return {'status': 'failure', 'operation': operation.key.urlsafe(), 'error': {'exception': 'InvalidURLError', 'message': str(e)}}

        except self.api.DownloadError, e:
            operation.status = 'error'
            operation.put()
            return {'status': 'failure', 'operation': operation.key.urlsafe(), 'error': {'exception': 'DownloadError', 'message': str(e)}}

        except self.api.ResponseTooLargeError, e:
            operation.status = 'error'
            operation.put()
            return {'status': 'failure', 'operation': operation.key.urlsafe(), 'error': {'exception': 'ResponseTooLargeError', 'message': str(e)}}

        else:

            # Store reference
            fetchdata = models.FetchedData(parent=okey, operation=okey, status_code=f.status_code, final_url=f.final_url, content=f.content, headers=dict([(str(k), str(v)) for k, v in f.headers.items()]), truncated=bool(f.content_was_truncated))
            dkey = fetchdata.put()

            operation.status = 'success'
            operation.data = dkey
            operation.put()

            return {'status': 'success', 'operation': operation.key.urlsafe(), 'result': {'status_code': f.status_code, 'data': dkey.urlsafe(), 'truncated': f.content_was_truncated, 'headers': dict([(str(k), str(v)) for k, v in f.headers.items()]), 'final_url': f.final_url}}


## PingURL - touch a URL and return only the status code and headers, discarding the content
class PingURL(URLFetchPipeline):

    ''' Retrieve a URL and yield a structure with the status code and response headers only. Content is discarded. '''

    def run(self):

        if 'http' not in url and 'https' not in url:
            try:
                key = ndb.Key(urlsafe=url)
            except:
                pass
            else:
                operation = key.get()
                url, payload, method, headers,
                allow_truncated, follow_redirects,
                deadline, validate_certificate =  operation.url, operation.payload, operation.method, operation.headers, operation.allow_truncated, operation.follow_redirects, operation.deadline, operation.validate_certificate

        else:
            operation = models.FetchOperation(**{
                'url': url,
                'payload': payload,
                'method': method,
                'headers': headers,
                'allow_truncated': allow_truncated,
                'follow_redirects': follow_redirects,
                'deadline': deadline,
                'validate_certificate': validate_certificate
            })
            okey = operation.put()

        if headers is None:
            headers = {}

        try:
            operation.status = 'fetching'
            operation.put()
            f = self.api.fetch(url, payload, method, headers, allow_truncated, follow_redirects, deadline, validate_certificate)

        except self.api.InvalidURLError, e:
            operation.status = 'error'
            operation.put()
            return {'status': 'failure', 'operation': operation.key.urlsafe(), 'error': {'exception': 'InvalidURLError', 'message': str(e)}}

        except self.api.DownloadError, e:
            operation.status = 'error'
            operation.put()
            return {'status': 'failure', 'operation': operation.key.urlsafe(), 'error': {'exception': 'DownloadError', 'message': str(e)}}

        except self.api.ResponseTooLargeError, e:
            operation.status = 'error'
            operation.put()
            return {'status': 'failure', 'operation': operation.key.urlsafe(), 'error': {'exception': 'ResponseTooLargeError', 'message': str(e)}}

        else:
            operation.status = 'success'
            operation.put()
            return {'status': 'success', 'operation': operation.key.urlsafe(), 'result': {'status_code': f.status_code, 'headers': f.headers, 'final_url': f.final_url}}
