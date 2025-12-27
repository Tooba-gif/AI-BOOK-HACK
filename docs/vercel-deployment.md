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
  ]
}
```

This configuration ensures that:
- The build output directory is set to `build`
- All routes are handled by the index.html file (important for client-side routing)

## Troubleshooting

If you encounter a 404 error after deployment:
1. Verify that the Root Directory is set to `frontend`
2. Ensure the Output Directory is set to `build`
3. Check that the build command is `npm run build`
4. Confirm that the `vercel.json` file exists in the frontend directory

## Additional Notes

- The frontend is built with Docusaurus, which generates static files in the `build` directory
- The site supports multiple languages (English and Urdu)
- Make sure to update the `url` and `baseUrl` in `docusaurus.config.js` to match your deployment URL