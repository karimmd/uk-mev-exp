#!/usr/bin/env python3

import json
import csv
import sys
from pathlib import Path

def extract_oid(id_obj):
    if isinstance(id_obj, dict) and '$oid' in id_obj:
        return id_obj['$oid']
    return str(id_obj) if id_obj else None

def convert_jsonl_to_csv(input_path, output_path, batch_size=10000):

    # Define CSV columns based on Ethereum transaction structure
    # Order matches typical usage: identifiers, sender/receiver, gas, value, then technical fields
    fieldnames = [
        # Primary identifiers
        '_id',
        'hash',
        'blockNumber',
        'blockHash',
        'transactionIndex',
        'timestamp',

        # Transaction participants
        'from',
        'to',
        'nonce',

        # Value and gas (critical for MEV analysis)
        'value',
        'gas',
        'gasPrice',
        'maxFeePerGas',        # EIP-1559
        'maxPriorityFeePerGas', # EIP-1559

        # Transaction data
        'input',
        'type',

        # Signature components
        'v',
        'r',
        's',

        # Additional fields
        'accessList',  # EIP-2930
        'chainId'
    ]

    print(f"Converting {input_path} to {output_path}")
    print(f"This may take a while for large files...")

    records_processed = 0
    records_written = 0
    errors = 0

    try:
        with open(input_path, 'r', encoding='utf-8') as infile, \
             open(output_path, 'w', newline='', encoding='utf-8') as outfile:

            writer = csv.DictWriter(outfile, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()

            for line_num, line in enumerate(infile, 1):
                try:
                    # Parse JSON line
                    record = json.loads(line.strip())
                    records_processed += 1

                    # Extract _id if it's a MongoDB ObjectId
                    if '_id' in record:
                        record['_id'] = extract_oid(record['_id'])

                    # Convert accessList to string if it exists
                    if 'accessList' in record and isinstance(record['accessList'], list):
                        record['accessList'] = json.dumps(record['accessList'])

                    # Write to CSV
                    writer.writerow(record)
                    records_written += 1

                    # Progress update
                    if records_processed % batch_size == 0:
                        print(f"Processed: {records_processed:,} records | Written: {records_written:,} | Errors: {errors}", flush=True)

                except json.JSONDecodeError as e:
                    errors += 1
                    print(f"Error parsing line {line_num}: {e}", file=sys.stderr)
                    if errors > 100:
                        print("Too many errors, stopping conversion", file=sys.stderr)
                        return False

                except Exception as e:
                    errors += 1
                    print(f"Error processing line {line_num}: {e}", file=sys.stderr)
                    if errors > 100:
                        print("Too many errors, stopping conversion", file=sys.stderr)
                        return False

        print(f"\n=== Conversion Complete ===")
        print(f"Total records processed: {records_processed:,}")
        print(f"Total records written: {records_written:,}")
        print(f"Total errors: {errors}")
        print(f"Output file: {output_path}")

        # Get output file size
        output_size = Path(output_path).stat().st_size
        print(f"Output file size: {output_size / (1024**3):.2f} GB")

        return True

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return False


if __name__ == "__main__":
    input_file = "<PROJECT_ROOT>/large/observed_transactions.json"
    output_file = "<PROJECT_ROOT>/large/observed_transactions.csv"

    # Check input file exists
    if not Path(input_file).exists():
        print(f"Error: Input file not found: {input_file}", file=sys.stderr)
        sys.exit(1)

    # Run conversion
    success = convert_jsonl_to_csv(input_file, output_file, batch_size=10000)

    sys.exit(0 if success else 1)
