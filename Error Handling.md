<h1>Standard Error Codes for API's</h1>

HTTP accomplishes this with five categories of status codes:

As the creator of my API, it's essential to handle errors effectively to ensure a positive user experience. 
My API should validate all incoming requests and return appropriate error responses if validation fails. 

The error message will be clear and concise, indicating the specific reason for the failure and providing actionable steps to resolve the issue. 
It's also important to use the appropriate HTTP status codes to indicate the severity of the error. 

Additionally, it's best practice to log all errors in your application, including the error message and stack trace, to help you diagnose and resolve any issues quickly. 
By following these best practices, I will ensure that my API provides a smooth and reliable experience for your users.

All fill return errors in a similar manner as the following

<ul>
<li>100-level (Informational) – server acknowledges a request</li>
<li>200-level (Success) – server completed the request as expected</li>
<li>300-level (Redirection) – client needs to perform further actions to complete the request</li>
<li>400-level (Client error) – client sent an invalid request</li>
<li>500-level (Server error) – server failed to fulfill a valid request due to an error with server</li>
</ul>
