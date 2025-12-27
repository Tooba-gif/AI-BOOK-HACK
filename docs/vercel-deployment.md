# Deploying the AI Textbook Frontend to Vercel

## Prerequisites
- A Vercel account (logged in at https://vercel.com)
- Access to the GitHub repository

## Deployment Steps

### Option 1: Using Vercel Dashboard (Recommended)

1. Go to https://vercel.com and ensure you're logged in
2. Click on "New Project" 
3. Select "Import Git Repository"
4. Choose your GitHub repository (Tooba-gif/AI-BOOK-HACK)
5. In the project configuration:
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `build`
   - Development Command: `npm run dev`
6. Click "Deploy"

### Option 2: Using Vercel CLI

1. Install the Vercel CLI globally:
   ```bash
   npm i -g vercel
   ```

2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

3. Deploy the project:
   ```bash
   vercel --prod
   ```

## Configuration Files

This project includes a `vercel.json` file in the frontend directory with the following configuration:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "build"
      }
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ],
  "github": {
    "enabled": true,
    "autoJobCancelation": true
  },
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        {
          "key": "Access-Control-Allow-Origin",
          "value": "*"
        },
        {
          "key": "Access-Control-Allow-Methods",
          "value": "GET, POST, PUT, DELETE, OPTIONS"
        },
        {
          "key": "Access-Control-Allow-Headers",
          "value": "Content-Type, Authorization"
        }
      ]
    }
  ]
}
```

This configuration ensures that:
- The build output directory is set to `build`
- All routes are handled by the index.html file (important for client-side routing)
- GitHub integration is enabled
- Proper headers are set for API requests

## Troubleshooting

If you encounter a 404 error after deployment:
1. Verify that the Root Directory is set to `frontend`
2. Ensure the Output Directory is set to `build`
3. Check that the build command is `npm run build`
4. Confirm that the `vercel.json` file exists in the frontend directory
5. Make sure you're accessing the root path, not a subdirectory
6. Check if your custom domain settings (if any) are properly configured

## Additional Notes

- The frontend is built with Docusaurus, which generates static files in the `build` directory
- The site supports multiple languages (English and Urdu)
- Make sure to update the `url` in `docusaurus.config.js` to match your deployment URL
- The baseUrl in `docusaurus.config.js` should remain as '/' for Vercel deployments
- After deployment, you may need to clear your browser cache to see the latest changes

## Redeployment

If you've made changes to your code:
1. Push the changes to your GitHub repository
2. Vercel will automatically redeploy if GitHub integration is enabled
3. Or manually trigger a redeployment from the Vercel dashboard