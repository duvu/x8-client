# Integration Testing Guide

## Running Integration Tests

The integration tests are designed to verify that the x8 client works correctly against the real API. Since these tests make actual API calls, they:

1. May be slow
2. Might incur costs
3. Could hit rate limits
4. Require proper credentials

### How to Run Integration Tests

```bash
# Run only integration tests
python run_tests.py --integration

# Run all tests including integration tests
python run_tests.py --all

# Run integration tests with coverage
python run_tests.py --integration --coverage
```

### Configuration

Integration tests use the credentials from your `.env` file. Make sure these are set correctly:

```
API_BASE_URL=https://your-api-url.com
SECRET_KEY=your_secret_key
```

### Best Practices

1. **Don't run in CI/CD automatically**: These tests should typically be run manually or in a separate CI job that's triggered explicitly
2. **Use test accounts**: If possible, use test credentials that don't affect production data
3. **Be mindful of rate limits**: Add delays between tests if necessary
4. **Clean up test data**: If your tests create data, consider adding cleanup code

### Adding New Integration Tests

When adding new tests:
1. Always mark with `@pytest.mark.integration`
2. For expensive operations, consider using `@pytest.mark.xfail`
3. Add good error messages that help diagnose API issues
4. Add proper assertions to verify the API behavior
