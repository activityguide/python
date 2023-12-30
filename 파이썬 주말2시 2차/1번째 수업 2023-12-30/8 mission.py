class Watch:
    def What(self):
        a = input('지금 몇시').split(":")
        self.hour = int(a[0])
        self.min = int(a[1])
        self.sec = int(a[2])

    def see(self):
        print(f'지금은 {watch.hour}시{watch.min}분{watch.sec}초 입니다')


watch = Watch()
watch.What()
watch.see()
