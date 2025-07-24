#!/usr/bin/env python3
"""
Main entry point for BriefWave.
This script runs the automation process to generate and email content summaries.
"""

import sys
from orchestrator import BriefWaveAutomator

def main():
    """Main function to run the BriefWave automation."""
    try:
        print("Starting BriefWave automation...")
        automator = BriefWaveAutomator()
        success = automator.run()
        
        if success:
            print("BriefWave completed successfully.")
            return 0
        else:
            print("BriefWave completed with errors.")
            return 1
    except Exception as e:
        print(f"Error running BriefWave: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
