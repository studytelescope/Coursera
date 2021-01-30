import requests
from matplotlib import pyplot as plt


def find_distribution(uid):
    distribution = {}
    for i in range(12):
        distribution['{index}'.format(index=i + 1)] = 0

    users_list = []
    service_id = 'a6024a04a6024a04a6024a04b7a6746b0aaa602a6024a04c612d3ae3389004bc3913dde'

    uid_link = 'https://api.vk.com/method/users.get?v=5.71&access_token='
    uid_link += service_id + '&user_ids=' + uid + '&fields=online'

    user = requests.get(uid_link)
    user_data = user.json()['response']
    user_id = user_data[0]['id']

    friends_url = 'https://api.vk.com/method/friends.get?v=5.71&access_token='
    friends_url += service_id + '&user_id=' + str(user_id) + '&fields=bdate'

    friends_response = requests.get(friends_url)
    friends = friends_response.json()['response']['items']

    for guy in friends:
        if "bdate" in guy:
            b_days = guy['bdate'].split('.')
            day = b_days[0]
            month = b_days[1]

            distribution[month] += 1

            users_list.append([guy['first_name'], guy['last_name'], day, month])

    return distribution


def build_distribution(distribution, user_name):
    y_axis = []
    x_axis = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    for i in range(12):
        y_axis.append(distribution['{index}'.format(index=i + 1)])

    plt.xlabel("Months")
    plt.ylabel("Number of people")
    plt.plot(x_axis, y_axis)
    plt.savefig('distribution_{name}.png'.format(name=user_name))
    plt.show()


if __name__ == '__main__':
    user_name = 'aya1508'
