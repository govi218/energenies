# Zebra-Zeal

Energenies, a gamified application for educating users about their energy usage and taking them through a prosumer's hero journey. 

Singular spectrum decomposition combined with a shallow neural network matches energy consumption patterns to actual devices.

Hardware devices employ homomorphic encryption to enable clustering and other aggregated learning.

## Privacy-Preserving Aggregation protocol

The application implements a privacy-preserving data aggregation protocol from Garcia, Flavio & Jacobs, Bart. (2010), "Privacy-Friendly Energy-Metering via Homomorphic Encryption" (https://www.cs.bham.ac.uk/~garciaf/publications/no-leakage.pdf). The protocol relies on Paillier's additively homomorphic encryption scheme allowing certain mathematical operations to be performed on encrypted data. The goal is to compute total consumption of a certain group of households, without leaking any information about their individual consumption.

Two types of parties take part in the protocol run. The 'Customer' is a representation of a household - a party with a smartmeter, generating consumption data. Customers are clustered into regions for which a total consumption is computed, without revealing any information about individual consumption data. Second party in the protocol is the 'Aggregator'. It is a party responsible for collecting encrypted readings from multiple Customers and adding them together into an intermediate consumption data for the whole region. Data sent to the Aggregator is encrypted and none of the parties can learn partial consumption contribution.

Customers split their meter reading data into as many random shares as Customers in the region. Each is then encrypted with public key of one Customer. One share is retained and not sent. This data is sent to the Aggregator, who receives such shares from each Customer. Shares encrypted with the same key are then added together and returned to the Customer who owns the key to decrypt them. Due to mixing of various shares, the Customers do not learn any valuable information about consumption of other individual Customers. After the Customer decrypts the data, the remaining share is added and final result of aggregation is produced. This information is returned to the Aggregator.

The protocol allows to detect malicious input to the Aggregator. If at least 2 parties from the region are honest and behave according to the protocol specification, the Aggregator will be able to detect incorrect readings and discard them. This does not influence the result of the total consumption, and still allows to obtain a correct measurement.

## Setting up application
<br/>

**Note**: application can be run by using `build.sh` script

<br/>

### [FOR DEVELOPMENT] Running develoment Flask server

1. Start pip virtual environment
2. Export environment variables: `export $(cat .env)`
3. Run the dev flask server using bash script `./build -dev`

<br/>

### [FOR STAGING LOCAL] Running as docker container

1. Export environment variables: `export $(cat .env)`
2. Run staging environment `./build.sh -stag`
3. Images are automatically pulled and set up
4. Access application on `localhost/join`

<br/>

### [FOR PRODUCTION REMOTE] 

1. Just don't for now, bad things will happen ;)

