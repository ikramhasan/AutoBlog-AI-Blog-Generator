 # Next.js Middleware: Extending Functionality with Custom Serverless Endpoints

## **Introduction**

Next.js is a popular React framework that offers built-in API routes for handling server-side logic. One way to further extend the functionality of Next.js is by using custom middleware and creating serverless endpoints. In this article, we will discuss how to create and use custom middleware with Next.js to build dynamic APIs.

## **What are Custom Serverless Endpoints?**

Custom serverless endpoints allow you to create APIs with specific functionality that can be integrated into your Next.js applications. These endpoints are serverless, meaning they run on demand and scale automatically as needed. Using custom middleware in Next.js is a powerful way to extend the capabilities of the framework and create more robust applications.

## **Creating Custom Middleware**

To create custom middleware for Next.js, you will write an Express-compatible middleware function. Here's a simple example:

```javascript
const myMiddleware = (req, res, next) => {
  // Your code here
  // ...

  next();
}

module.exports = myMiddleware;
```

## **Using Custom Middleware with Next.js**

To use custom middleware in a Next.js API route, you will import the middleware function and wrap it around your handler function:

```javascript
import myMiddleware from './my-middleware';

export const config = {
  api: { bodyParser: false }, // Disable body-parser to allow Express-style request handling
};

export default (req, res) => {
  myMiddleware(req, res, next => {
    // Your API logic here
    // ...

    res.status(200).json({ message: 'Hello, world!' });
  });
}
```

## **Practical Example: Building an API with Custom Serverless Endpoints**

In this example, we will create a custom middleware for handling authentication and an API route for retrieving user data.

1. Initialize the project and install dependencies:

   ```bash
   npx create-next-app my-app
   cd my-app
   npm install express next-routes serverless-http
   ```

2. Create a custom middleware file (`lib/middleware.js`) for handling authentication:

   ```javascript
   const jwt = require('jsonwebtoken');

   module.exports = function (req, res, next) {
     const token = req.headers.authorization && req.headers.authorization.split(' ')[1];

     if (!token) {
       return res.status(401).json({ error: 'No token provided' });
     }

     try {
       const decoded = jwt.verify(token, process.env.JWT_SECRET);
       req.user = decoded;
       next();
     } catch (err) {
       return res.status(401).json({ error: 'Invalid or expired token' });
     }
   };
   ```

3. Set up the API route file (`pages/api/users/index.js`) and import the custom middleware:

   ```javascript
   import myMiddleware from '../../lib/middleware';

   export const config = {
     api: { bodyParser: false },
   };

   export default (req, res) => {
     myMiddleware(req, res, () => {
       // Your API logic here
       // ...

       res.status(200).json({ message: 'User data', data: { name: 'John Doe' } });
     });
   };
   ```

4. Test the custom serverless endpoint using tools like Postman or cURL:

   Make sure to include the JWT token in the Authorization header of your request to test the middleware functionality.

## **Benefits of Custom Serverless Endpoints**

Using custom serverless endpoints with Next.js middleware provides several benefits, including:

1. Enhancing functionality without leaving the ecosystem: By staying within the Next.js ecosystem, you can easily manage and maintain your application's functionality in a single place.
2. Scalability and performance improvements: Custom serverless endpoints offer better scalability and performance by allowing you to handle specific functions independently and only paying for the resources consumed.
3. Improved flexibility and maintainability: With custom serverless endpoints, you have more control over your application's logic and can create dynamic APIs tailored to your unique needs.