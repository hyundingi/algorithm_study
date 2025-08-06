class MyQueue(object):

    def __init__(self):        # 생성자
        self.stack_in = []     # 데이터를 넣을 때 사용하는 스택
        self.stack_out = []    # 데이터를 뺄 때 사용하는 스택 (임시 저장소)
        
	# -> 표시는 파이썬 3.5 부터 적용된 리턴 값에 대한 힌트 개념
    # 즉 이 함수는 아무것도 반환하지 않는다 라는 뜻
    def push(self, x: int) -> None: # 데이터를 넣는 함수
    # def push(self, x): 이렇게 해도 코드는 실행됨
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        

    def pop(self) -> int:             # 큐에서 맨 앞에 있는 값을 꺼냄 (dequeue)
        """
        :rtype: int
        """
       while self.stack_in:    # stack_in 리스트에 값이 있을 때까지
       	self.stack_out.append(self.stack_in.pop()) # stack_out 에 in의 역순으로 값이 담김
       
       front_value = self.stack_out.pop()
       
       while self.stack_out:   # 원상복구
       	self.stack_in.append(self.stack_out.pop())
       
       return front_value

        

    def peek(self) -> int:      # 가장 먼저 들어온 값을 보여줌 (front)
        """
        :rtype: int
        """
        return self.stack_in[0]
        

    def empty(self) -> bool:
        """
        :rtype: bool
        """
        return len(self.stack_in) == 0 
        

# 내부적으로 하는 일 (직접 실행하지 않아도 됨)
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()