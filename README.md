# AWS Lambda Deploy with GitHub Actions (OIDC)

This repository demonstrates a secure CI/CD pipeline that deploys a simple AWS Lambda function using GitHub Actions and OpenID Connect (OIDC). No static AWS credentials are stored in GitHub. Each run requests a short-lived token from GitHub and exchanges it for temporary AWS credentials through an IAM role whose trust policy accepts only the `main` branch of this repository.

## Contents

- `lambda_function.py`: a minimal Python handler that returns a JSON greeting.
- `.github/workflows/main.yml`: the deploy pipeline that packages the function and runs `aws lambda update-function-code` on every push to `main`.

## How it works

1. The workflow requests an OIDC token (`id-token: write`).
2. `aws-actions/configure-aws-credentials@v4` assumes the IAM role defined in the `AWS_ROLE_ARN` repository variable.
3. The function code is zipped and pushed to the Lambda named in the `AWS_LAMBDA_NAME` variable.

## Required repository variables

Configure these under Settings, Secrets and variables, Actions, Variables:

- `AWS_ROLE_ARN`: ARN of the IAM role that GitHub Actions assumes.
- `AWS_REGION`: target region (for example `us-east-1`).
- `AWS_LAMBDA_NAME`: name of the Lambda function to update.

## IAM trust relationship

The role trusts the GitHub OIDC provider and restricts the `sub` claim to one repository and branch. Repositories created after July 15, 2026 use the immutable subject claim format, which embeds the numeric owner and repository IDs, as described in [Immutable subject claims for GitHub Actions OIDC tokens](https://github.blog/changelog/2026-04-23-immutable-subject-claims-for-github-actions-oidc-tokens/).

## Related article

This repository accompanies a tutorial on building a secure deployment pipeline for AWS Lambda using GitHub Actions.
