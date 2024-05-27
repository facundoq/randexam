import numpy as np
import enum

class Discretization(enum.Enum):
    frequency="frequency"
    range="range"

def discretize(values,n_intervals:int,strategy:Discretization):
    if strategy==Discretization.frequency:
        return discretize_by_frequency(values,n_intervals)
    elif strategy==Discretization.range:
        return discretize_by_range(values,n_intervals)
    else:
        raise ValueError(strategy)
    


class Interval:
    def __init__(self,start,end,include_end=False):
        self.start=start
        self.end=end
        self.include_end=include_end
    def contains(self,v):
        if self.include_end:
            return self.start<=v and v<=self.end
        else:
            return self.start<=v and v<self.end
    def __repr__(self):
        end_sign= "]" if self.include_end else ")"
        return f"[{self.start},{self.end}{end_sign}"


def discretize_value(v,intervals:[Interval],values:list):
    for i,interval in enumerate(intervals):
        if interval.contains(v):
            return values[i]
    raise ValueError(f"No interval defined for value {v}")

def discretize_values(x,intervals:[Interval],values:list):
    return [discretize_value(v,intervals,values) for v in x]


def discretize_by_range(x,values:list):
    
    n_intervals=len(values)
    x=np.array(x)
    mi,ma=x.min(),x.max()
    interval_size=(ma-mi)/n_intervals
    intervals=[]
    for i in range(n_intervals):
        start=mi+(i*interval_size)
        end=start+interval_size
        start=round(start,2)
        end=round(end,2)
        include_end= i==(n_intervals-1)
        
        interval=Interval(start,end,include_end=include_end)
        intervals.append(interval)
    
    return intervals,discretize_values(x,intervals,values)



def discretize_by_frequency(x,values:list):
    
    n_intervals=len(values)
    x=np.array(x)
    sorted_values=sorted(x)
    n=len(x)
    
    interval_indexes=np.linspace(0,n-1,n_intervals,endpoint=False)
    interval_indexes=[int(np.ceil(i)) for i in interval_indexes]
    intervals=[]
    for i in range(n_intervals):
        start=sorted_values[interval_indexes[i]]
        if i==n_intervals-1:
            end=sorted_values[-1]
            intervals.append(Interval(start,end,include_end=True))
        else:
            end=sorted_values[interval_indexes[i+1]]
            intervals.append(Interval(start,end))

    return intervals,discretize_values(x,intervals,values)



class CenterScaleNormalization:
    def __init__(self,center:float,scale:float):
        self.center=center
        self.scale=scale
    def apply(self,values:np.ndarray)->np.ndarray:
        values=values.copy()
        for i in range(len(values)):
            values[i]=(values[i]-self.center)/self.scale
        return values
    @classmethod
    def min_max(cls,values):
        center=values.min()
        ma=values.max()
        scale=ma-center
        return CenterScaleNormalization(center,scale)
    @classmethod
    def mu_std(cls,values):
        return CenterScaleNormalization(values.mean(),values.std())

    def __repr__(self):
        return f"(x-{self.center:.2f})/{self.scale:.2f}"
