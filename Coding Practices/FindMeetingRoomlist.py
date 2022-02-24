
# meeting room details which is dictionary of room number as key and value is list of two values starting and ending time of the meeting
# OccupiedRoomDetails = {0 : ["9AM", "11AM"], 1: ["10AM", "12AM"], 2: ["11AM", "12AM"], 3: ["9AM", "10AM"]}


def FindMeetingRoomlist(TimeInstance):        
    arr = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1,0, 0, 0], [1, 1, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 0, 1]]
    hour_dict = {"9AM" : 0, "10AM" : 1, "11AM" : 2, "12AM" : 3, "1PM" : 4, "2PM" : 5, "3PM" : 6, "4PM" : 7, "5PM" : 8, "6PM" : 9}
    result = []
    # print(arr[3])
    for i in range(len(arr)):
        if(arr[i][hour_dict[TimeInstance]] == 0):    
            result.append(i+1)
    return result









print(FindMeetingRoomlist("10AM")) #[3, 4, 6, 8]