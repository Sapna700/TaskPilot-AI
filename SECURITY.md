# Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability in TaskPilot-AI, please report it responsibly to us instead of using the public issue tracker.

### How to Report

Please email your security concerns to: **[sapna@taskpilot.dev](mailto:sapna@taskpilot.dev)**

Include the following information in your report:

- Description of the vulnerability
- Steps to reproduce the issue
- Potential impact
- Any suggested fixes (if you have them)

### Response Timeline

- We will acknowledge receipt of your report within 48 hours
- We will work on a fix and provide you with a timeline
- We will notify you when the security patch is released
- We will credit you in the security advisory (unless you prefer to remain anonymous)

### Scope

We take security seriously for:
- Core TaskPilot-AI code
- Dependencies and third-party libraries
- API integrations (especially OpenAI API handling)

## Best Practices for Users

To keep your TaskPilot-AI installation secure:

1. **Keep dependencies updated**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Protect your API keys**
   - Never commit `.env` files to version control
   - Use `.env.example` as a template
   - Rotate API keys regularly
   - Use environment variables in production

3. **Use secure authentication**
   - Keep your OpenAI API key confidential
   - Don't share credentials in bug reports

4. **Review code changes**
   - Review pull requests before merging
   - Run tests before deployment
   - Use branch protection rules

## Supported Versions

| Version | Status | Security Updates |
|---------|--------|------------------|
| 0.1.x   | Current | Yes |

We recommend always using the latest version for security patches.

## Security Headers and Best Practices

- Always validate user input
- Sanitize API responses
- Never log sensitive information (API keys, tokens)
- Use HTTPS for any web-based features
- Follow OWASP guidelines

## License

This security policy is provided under the MIT License.

---

Thank you for helping us keep TaskPilot-AI secure! 🔒
