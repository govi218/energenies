from phe import paillier
import string 
import random 
import csv
import sys
import numpy as np

customer_number = 5

############### --- MAIN --- #######################
def main():

    # Initialize users
    aggregator = Aggregator()
    customers = []
    for i in range(customer_number):
        customers.append(Customer(aggregator))
    
    for i in range(len(customers)):
        enc_shares = customers[i].encrypt_shares()
        customers[i].send_enc_shares(enc_shares)

    aggragation_result = aggregator.aggregate_data()
    
    total_Paillier = 0
    for uuid in aggragation_result:
        for customer in customers:
            if uuid is customer.name:
                aggr_ptxt = customer.private_key.decrypt(aggragation_result[uuid])
                aggr_ptxt += customer.retained_share
                total_Paillier += aggr_ptxt
                print("Sum of shares for user {}: {}".format(uuid, aggr_ptxt))

    print("Generated sum: ", Customer.smartmeter_reading_sum)
    print("Aggregated sum: ", total_Paillier)



############### --- END MAIN --- #######################




# HELPER FUNC
# Merge dictionaries and keep values of common keys in list
def mergeDict(input):
    result_dict = {}
    for dictionary in input:
        for key, value in dictionary.items():
            if key not in result_dict:
                result_dict[key] = list()
            result_dict[key].append(value)
    return result_dict


def get_key(my_dict, val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
    return "key doesn't exist"



# Party receiving the data
class Aggregator():
    def __init__(self):
        self.key_gen()
        self.name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 8)) 
        self.list_of_pubkeys = {}
        self.aggregation_input = []

    def key_gen(self):
        self.public_key, self.private_key = paillier.generate_paillier_keypair()


    # Obtain data from Customers and add it all together
    # Sum all records encrypted with one key
    # Input comes as a list of dictionaries. Merge dictionaries together and sum up all the values encrypted with corresponding public key
    def aggregate_data(self):
               
        # Dictionary merging
        temp_dict = mergeDict(self.aggregation_input)

        # For each ctxt per key, sum them up together
        sum_ctxt = {}
        for x in temp_dict:
            sum_ctxt[x] = sum(temp_dict[x])

        return sum_ctxt


    def set_public_key(self, UUID, pubkey):
        self.list_of_pubkeys[UUID] = pubkey


    def get_public_keys(self):
        return dict(self.list_of_pubkeys)



# Party generating the smartmeter data
class Customer():

    smartmeter_reading_sum = 0

    def __init__(self):
        self.key_gen()
        self.name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 8)) 

    def __init__(self, aggregator, reading):
        self.key_gen()
        self.name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 8)) 
        self.aggregator = aggregator
        self.reading = reading
        Customer.smartmeter_reading_sum += self.reading
        print("Smartmeter reading for user {} : {}".format(self.name, self.reading))
        aggregator.set_public_key(self.name, self.public_key)


    # Generate Paillier key pair
    def key_gen(self):
        self.public_key, self.private_key = paillier.generate_paillier_keypair()


    # Generate a mock meter reading.
    def get_meter_reading(self):
        Customer.smartmeter_reading_sum += self.reading
        print("Smartmeter reading for user {} : {}".format(self.name, self.reading))
        return self.reading


    # Obtain a meter reading and split into $numer_of_splits shares
    def split_meter_reading(self, number_of_splits):
        self.reading_shares = (np.random.dirichlet( np.ones(number_of_splits), size=1) * self.reading)[0]
        return self.reading_shares


    # Encrypt each share of own reading with own public key
    def encrypt_shares(self, public_keys = []):
        if not public_keys:
            public_keys = self.aggregator.get_public_keys()
            del public_keys[self.name]

        ctxt_arr = {}
        self.split_meter_reading(len(public_keys) +1)
        
        # Witheld last share and do not encrypt with own key.
        index = 0
        for i in public_keys:
            if i not in ctxt_arr:
                ctxt_arr[i] = list()
            # UUID for pubkey reference, ctxt
            ctxt_arr[i] = public_keys.get(i).encrypt(self.reading_shares[index])
            index += 1
        self.retained_share = self.reading_shares[-1]
        return ctxt_arr


    # Send encrypted shares to Aggregator
    def send_enc_shares(self, input):
        self.aggregator.aggregation_input.append(input)


# Main function call
if __name__ == "__main__":
    main()