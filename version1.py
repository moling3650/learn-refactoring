#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-21 11:09:22
# @Author  : moling (365024424@qq.com)
# @Link    : http://www.qiangtaoli.com
# @Version : 1


class Movie(object):

    """docstring for Movie"""
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self._title = title
        self._price_code = price_code

    def get_price_code(self):
        return self._price_code

    def set_price_code(self, price_code):
        self._price_code = price_code

    def get_title(self):
        return self._title


class Rental(object):

    """Rental"""

    def __init__(self, movie, days_rented):
        self._movie = movie
        self._days_rented = days_rented

    def get_days_rented(self):
        return self._days_rented

    def get_movie(self):
        return self._movie


class Customer(object):

    """docstring for Customer"""

    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, rental):
        self._rentals.append(rental)

    def get_name(self):
        return self._name

    def statament(self):
        total_amount = 0.0
        frequent_renter_points = 0
        result = 'Rental Record for ' + self._name + '\n'
        for each in self._rentals:
            this_amount = 0.0
            # determine amounts for each rental
            if each.get_movie().get_price_code() == Movie.REGULAR:
                this_amount += 2
                if each.get_days_rented() > 2:
                    this_amount += (each.get_days_rented() - 2) * 1.5
            elif each.get_movie().get_price_code() == Movie.NEW_RELEASE:
                this_amount += each.get_days_rented() * 3
            elif each.get_movie().get_price_code() == Movie.CHILDRENS:
                this_amount += 1.5
                if each.get_days_rented() > 3:
                    this_amount += (each.get_days_rented() - 3) * 1.5

            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two day new release rental
            if each.get_movie().get_price_code() == Movie.NEW_RELEASE and each.get_days_rented() > 1:
                frequent_renter_points += 1

            # show figures for this rental
            result += '\t' + each.get_movie().get_title() + '\t' + str(this_amount) + '\n'
            total_amount += this_amount
        # add footer lines
        result += 'Amount owed is ' + str(total_amount) + '\n'
        result += 'You earned ' + str(frequent_renter_points) + ' frequent renter points'
        return result

if __name__ == '__main__':
    c = Customer('moling')
    c.add_rental(Rental(Movie('Zootopia', 2), 7))
    c.add_rental(Rental(Movie('The Finest Hours', 0), 3))
    c.add_rental(Rental(Movie('Angry Birds', 1), 2))
    print(c.statament())
