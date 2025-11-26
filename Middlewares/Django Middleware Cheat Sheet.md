# Django Middleware Cheat Sheet

### 

### What is Middleware?

Middleware is a \*\*layer of code between the request and response\*\* in Django.  

It can \*\*inspect, modify, or block requests/responses\*\* globally before they reach the view or after they leave it.



---



##### Basic Structure



###### ```python

###### class MyMiddleware:

###### &nbsp;   def \_\_init\_\_(self, get\_response):

###### &nbsp;       self.get\_response = get\_response

###### 

###### &nbsp;   def \_\_call\_\_(self, request):

###### &nbsp;       # Request logic

###### &nbsp;       response = self.get\_response(request)

###### &nbsp;       # Response logic

###### &nbsp;       return response

###### \_\_init\_\_ → runs once when Django starts

###### 

###### \_\_call\_\_ → runs for every request



##### Why Middleware is Useful

* Middleware handles cross-cutting concerns in one place:
* Authentication \& Authorization → validate tokens or sessions
* Logging \& Monitoring → track request paths, durations, status codes
* Security → add headers like X-Frame-Options, Content-Security-Policy
* Performance → caching, compression
* Request/Response Modification → inject or alter data globally



Real-World Examples

Use Case	Example

Authentication	API token check for all endpoints

Logging		Log request time and status

Security	Add HTTP security headers automatically

Caching		Cache HTML or API responses

Feature Flags	Enable/disable features per request



**Key Takeaways**



* Middleware runs on every request and response.
* Ideal for global behaviors across multiple views.
* Reduces code duplication \& improves maintainability.
* Order matters — controlled via MIDDLEWARE setting.
