#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
import os, sys, argparse, math

class MathUtils():

    def divisible_by(self, number, return_type):
        """ Returns the sum of a list of numbers , or the list itself divisible to the input. """
        divisible_sum = 0
        divisible_list = []
        for x in xrange(1, number):
            if number % x == 0:
                divisible_sum += x
                divisible_list.append(x)

        if return_type=='sum':
            return divisible_sum
        else:
            return divisible_list

    def list_amicable(self, number):
        """ Returns a sum of a list of amicable number given a range. """
        amicable_sum = 0
        sum_rl = 0
        sum_lr = 0
        for x in xrange(number, 0, -1):
            sum_rl = self.divisible_by(x,'sum')
            sum_lr = self.divisible_by(sum_rl,'sum')
            if x == sum_lr and sum_rl != sum_lr:
                #print x , sum_rl, sum_lr, amicable_sum
                amicable_sum += x

        return amicable_sum

    def perfection(self, number):
        if number == self.divisible_by(number,'sum'):
            return 'perfect'
        elif number > self.divisible_by(number,'sum'):
            return 'abundant'
        else:
            return 'deficient'

    def abundance(self, number):
        pass


    def is_odd(self, number):
        v = True
        if number % 2==0:
            v = False
        return v

    def isprime(self, number):
        numnber = abs(int(number))
        if number < 2 : return False
        if number == 2 : return True
        if not number & 1 : return False
        for x in range (3 , int(number**0.5)+1, 2):
            if number % x == 0:
                return False
        return True

    def next_prime(self, number):
         number = number +1
         while number:
            if self.isprime(number):
                return number
                break
            number += 1

    def ith_prime(self, number):
        x = 2
        count = 1
        while count < number :
            if self.isprime(x):
                x = self.next_prime(x)
                print "count:", count ,"prime:", x
                count +=1
        return x

    def list_primes_till(self, number):
        prime  = 2
        while prime < number:
            print prime,
            prime = self.next_prime(prime)


    def sum_of_primes(self, number):
        """Returns the sum of primes up to input number."""

        skip = 1
        sum_ = 0
        for x in xrange( 2, number+1, skip):
            if self.isprime(x):
                skip = self.next_prime(x)
                sum_ += x
                print "prime",x , "sum = ",sum_
        return sum_

    def sum_of_first_primes(self, number):
        """Returns the sum of first primes up to input number. """

        sum_ = 0
        prime = 2
        counter = 0
        while counter < number:
            if self.isprime(prime):
                sum_ += prime
                counter += 1
                prime = self.next_prime(prime)
                print " counter",counter , " prime",prime , " sum = ",sum_
        return sum_

    def prime_factor(self, number):
        if number <1: sys.exit(1)
        if number >=1:
            prime_factor = []
            skip =1
            for i in xrange(2, int(number**0.5)+1 ,skip):
                if self.isprime(i):
                    print "prime:", i,"factor", prime_factor
                    skip = i
                    if number % i == 0:
                        print "factor:", i
                        prime_factor.append(i)
                    if len(prime_factor) > 10:
                        prime_factor.popleft()
                        print set(prime_factor)

        return set(prime_factor)

    def is_palindrome(self, product):
        print product
        if len(product) < 2: return True
        if product[0] != product[-1]: return False

        return is_palindrome(product[-1:1])

    def sumsq_difference_sqsum(self, number):
        sumi = 0
        sqsum = 0
        for i in range(1, number+1):
            sumi += i
            sqsum += i**2
        #   print i, sumi , sqsum, sumi**2, sumi**2 - sqsum
        return (sumi**2 - sqsum)

    def factorial(self, number):
        factorial =1
        for i in range (1, number + 1):
            factorial *= i
        return factorial

    def smallest_divisible(self, number):
        common_multiple = self.factorial(number)
        for i in xrange(number, 1, -1):
            if common_multiple % i == 0 and self.isprime(i):
                common_multiple  = common_multiple / i
                print common_multiple
        return common_multiple

    def run(self, util, number):
        if util == 'next_prime':
            print  self.next_prime(number)
        elif util == 'prime_factor':
            print  self.prime_factor(number)
        elif util == 'is_odd':
            print self.is_odd(number)
        elif util == 'isprime':
            print self.isprime(number)
        elif util == 'largest_palindrome':
            print  self.largest_palindrome(number)
        elif util == 'sumsq_sqsum':
            print self.sumsq_difference_sqsum(number)
        elif util == 'ith_prime':
            print self.ith_prime(number)
        elif util == 'sum_of_primes':
            print self.sum_of_primes(number)
        elif util == 'sum_of_first_primes':
            print self.sum_of_first_primes(number)
        elif util == 'smallest_divisible':
            print self.smallest_divisible(number)
        elif util == 'list_primes_till':
            print self.list_primes_till(number)
        elif util == 'list_amicable':
            print self.list_amicable(number)
        else:
            print ' i dont understand'
            sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("util")
    parser.add_argument("number")
    args = parser.parse_args()

    m = MathUtils()

    m.run(args.util, int(args.number) )

