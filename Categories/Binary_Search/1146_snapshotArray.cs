public class SnapshotArray {

    public int snapId = 0;
    Dictionary<int, List<List<int>>> rcd = new Dictionary<int, List<List<int>>>();
    int size;

    public SnapshotArray(int length) {
        size = length;
    }
    
    public void Set(int index, int val) {
        if (!rcd.ContainsKey(index)) {
            rcd.Add(index, new List<List<int>>());
            rcd[index].Add(new List<int> {snapId, val});
        }

        int listSize = rcd[index].Count;
        if (rcd[index][listSize - 1][0] == snapId){
            rcd[index][listSize - 1][1] = val;
        } else {
            rcd[index].Add(new List<int> {snapId, val});
        }
    }
    
    public int Snap() {
        int ret = snapId;
        snapId += 1;
        return ret;
    }
    
    public int Get(int index, int snap_id) {
        // error handling
        if (index >= size) {
            return -1;    
        }
        
        if (!rcd.ContainsKey(index)) {
            return 0;
        }

        int mid;
        int left = 0, right = rcd[index].Count - 1;
        while (left < right) {
            mid = left + (right -left) / 2 + 1;
            if (rcd[index][mid][0] > snap_id) {
                right = mid - 1;
            }
            else {
                left = mid;
            }
        }

        if (rcd[index][left][0] > snap_id) {
            return 0;
        }

        return rcd[index][left][1];
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.Set(index,val);
 * int param_2 = obj.Snap();
 * int param_3 = obj.Get(index,snap_id);
 */