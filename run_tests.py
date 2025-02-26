#!/usr/bin/env python
"""Test launcher for x8-client.

This script provides easy commands to run different types of tests.
"""

import argparse
import subprocess
import sys

def main():
    """Run the tests based on command line arguments."""
    parser = argparse.ArgumentParser(description="Run x8-client tests")
    parser.add_argument("--integration", action="store_true", 
                        help="Run integration tests that make real API calls")
    parser.add_argument("--all", action="store_true",
                        help="Run both unit and integration tests")
    parser.add_argument("--coverage", action="store_true",
                        help="Generate test coverage report")
    args = parser.parse_args()
    
    cmd = ["pytest"]
    
    if args.coverage:
        cmd.extend(["--cov=x8", "--cov-report=term", "--cov-report=html"])
    
    if args.all:
        # Run all tests
        pass
    elif args.integration:
        # Run only integration tests
        cmd.append("-m integration")
    else:
        # By default, skip integration tests
        cmd.append("-m 'not integration'")
    
    result = subprocess.run(cmd)
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
