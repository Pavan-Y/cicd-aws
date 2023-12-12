# cicd-aws
This is a simple project which includes complete CICD of a application in amazon web services.

## Architecture:
![Architrcture](https://github.com/Pavan-Y/cicd-aws/blob/main/cicd_on_aws.jpg)


This is an end-to-end ops pipeline in Amazon web services that can be used for any application. 



Used the following services:

### CodePipeline: 
Think of it as a project manager. It coordinates different tasks for your software's journey from creation to running live. It uses other tools like CodeBuild and CodeDeploy to manage each step effectively. This will come into action once there's a commit in the specified git repository.



### CodeBuild: 
Think of this as a workshop where you can assemble your software. Here, we instructed it to build a Docker image and push it into a private repository in ECR



### CodeDeploy: 
This is your deployment manager. When the codebuild part is done and the image is ready, CodeDeploy ensures it's delivered to the right destination which is ECS in this case.

### ECR:
This is the place where our docker images are stored, We'll be storing and updating the most recent image for each new commit using the 'latest' tag.

### ECS: 
This is the environment where our application runs. Instead of relying on changing IP addresses of ECS tasks, it's better to use a load balancer to communicate with it, acting as a receptionist who always knows where your workspace is.



By making use of the above services we built a complete end-to-end seamless pipeline. This setup is cost-optimized by leveraging on-demand cloud services, ensuring expenses align with actual usage.