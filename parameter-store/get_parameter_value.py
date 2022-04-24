import boto3
import pprint


PROFILE_NAME = 'yuki'
REGION_NAME = 'us-west-1'
PARAMETER = 'budget'


def main():

    session = boto3.session.Session(profile_name=PROFILE_NAME)
    ssm = session.client('ssm', region_name=REGION_NAME)
    response = ssm.get_parameters(
        Names=[PARAMETER],
        WithDecryption=True
    )
    print('Response')
    pprint.pprint(response)

    name = response['Parameters'][0]['Name']
    value = int(response['Parameters'][0]['Value'])
    print(f'{name}: {value}')


if __name__ == '__main__':
    main()
