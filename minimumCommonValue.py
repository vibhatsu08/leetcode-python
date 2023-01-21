# Minimum Common Value
# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

def getCommon (nums1, nums2) :
    i, j = 0, 0
    while (i<len(nums1) and (j<len(nums2))) :
        if nums1[i] == nums2[j] :
            return nums1[i]
        elif nums1[i] < nums2[j] :
            i += 1
        else :
            j += 1
    return -1
        
print(getCommon(nums1 = [1,2,3], nums2 = [2,4]))