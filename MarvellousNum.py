def ChkPrime(arr) :
	brr=list();
	brr.append(0);
	for j in arr : 
		num=j;
		count=0;
		i=2;
		while i < num :
			res=num%i;
			if res == 0 :
				count=count+1;
				break;
			else:
				pass;
			i=i+1;
			
		if count == 0 :
			brr.append(num);
		else :
			pass;

	print("Addition of Prime Numbers : ",sum(brr));