class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        return not (rec1[2] <= rec2[0] or rec1[0] >= rec2[3] or rec1[1] >= rec2[3] or rec1[3] <= rec2[1])