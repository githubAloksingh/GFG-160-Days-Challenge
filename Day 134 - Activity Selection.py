class Solution:
    def activitySelection(self, start, finish):
        #code here
        n=len(start)
        activities=[]
        for i in range(n):
            activities.append((finish[i],start[i]))
        activities.sort()
        count=0
        last_finish=-1
        for i in range(len(activities)):
            activity=activities[i]
            if activity[1]>last_finish:
                last_finish=activity[0]
                count+=1
        return count
#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the start times
        start = list(map(int, input().strip().split()))

        # Read the finish times
        finish = list(map(int, input().strip().split()))

        # Create solution object and call activitySelection
        obj = Solution()
        print(obj.activitySelection(start, finish))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
