
# meeting room details which is dictionary of room number as key and value is list of two values starting and ending time of the meeting
# OccupiedRoomDetails = {0 : ["9AM", "11AM"], 1: ["10AM", "12AM"], 2: ["11AM", "12AM"], 3: ["9AM", "10AM"]}
# Assuming requested meeting is only of 1 hour.

def FindMeetingRoomlist(starttime, endtime):        
    arr = [[1, 1, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 0, 1], [1, 0, 0, 1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]]
    hour_dict = {"9AM" : 0, "10AM" : 1, "11AM" : 2, "12AM" : 3, "1PM" : 4, "2PM" : 5, "3PM" : 6, "4PM" : 7, "5PM" : 8, "6PM" : 9}
    result = []
    for i in range(len(arr)):
        cnt = 0
        hours = (hour_dict[endtime] - hour_dict[starttime]) 
        j = hour_dict[starttime]
        while(cnt < hours and (arr[i][j] == 0)):
            cnt += 1
            if(j < 9):    
                j += 1
            else:
                break
            if(cnt == hours):
                result.append(i+1)
    return result


print(FindMeetingRoomlist("1PM", "2PM")) #[3, 4, 6, 8]