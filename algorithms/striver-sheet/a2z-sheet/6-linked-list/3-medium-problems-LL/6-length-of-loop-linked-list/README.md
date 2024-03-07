We will use Floyd's cycle detection algorithm , tortoise and hare to find a loop using slow and fast
pointer and once we find that loop exists we simply move slow pointer again from point of collision
till it comes back to fast pointer updating a len counter and when the slow and fast pointer meet
again the len will give us the result.