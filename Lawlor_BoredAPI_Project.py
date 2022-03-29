# Brenden Lawlor
# 11/20/21
# Assignment 14


# Working with APIs

# This program uses the Bored API at boredapi.com to allow the user to input a type of activity
# and have the program return a specific activity the user could try based on their activity
# type. Alternatively, the user also can just get a completely random activity if they wish.

import json
import requests


def main():
    keep_going = True
    while keep_going == True:
        print("This program will allow you to choose an activity type, then the program will suggest an activity to relieve your boredom.")
        activity_type = get_activity_type()
        url = get_url(activity_type)
        response = get_activity(url)
        display_activity(response)

        keep_going_yn = input(
            "Would you like a new activity suggested? (y/n): ")
        while keep_going_yn != 'y' and keep_going_yn != 'n':
            print(keep_going_yn)
            print("Please enter 'y' or 'n'.")
            keep_going_yn = input(
                "Would you like a new activity suggested? (y/n): ")

        if keep_going_yn == 'n':
            keep_going = False


def get_activity_type():
    valid_responses = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    keep_going = True
    while keep_going == True:
        print("\t------MENU------\n\tEducation:    0\n\tRecreational: 1\n\tSocial:       2\n\tDIY:\t      3\n\tCharity:      4"
              "\n\tCooking:      5\n\tRelaxation:   6\n\tMusic:        7\n\tBusywork:     8\n\tRandom Type:  9")

        activity_type = input("Please enter a number from the MENU above: ")

        if activity_type not in valid_responses:
            print("\nInvalid response received. Please look at the MENU and try again.")
        else:
            keep_going = False
    return activity_type


def get_url(activity_type):
    base_url = 'http://www.boredapi.com/api/activity/'

    # not sure if there is a better way to do this but if there is please let me know
    if activity_type == '0':
        url = base_url + '?type=education'
    elif activity_type == '1':
        url = base_url + '?type=recreational'
    elif activity_type == '2':
        url = base_url + '?type=social'
    elif activity_type == '3':
        url = base_url + '?type=diy'
    elif activity_type == '4':
        url = base_url + '?type=charity'
    elif activity_type == '5':
        url = base_url + '?type=cooking'
    elif activity_type == '6':
        url = base_url + '?type=relaxation'
    elif activity_type == '7':
        url = base_url + '?type=music'
    elif activity_type == '8':
        url = base_url + '?type=busywork'
    elif activity_type == '9':
        url = base_url

    return(url)


def get_activity(url):
    r = requests.get(url)
    response = r.json()
    return response


def display_activity(response):
    print(
        f'Your suggested {response["type"]} activity is "{response["activity"]}".')


main()
