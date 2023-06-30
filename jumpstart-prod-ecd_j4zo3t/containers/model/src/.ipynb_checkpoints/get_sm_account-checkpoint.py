import argparse
import sagemaker


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--region', type=str)
    parser.add_argument('--framework', type=str)
    args = parser.parse_args()
    
    registry = sagemaker.image_uris.retrieve(
        region=args.region,
        framework=args.framework,
        version='0.20.0',
    )
    account_id = registry.split('.')[0]
    print(account_id)
