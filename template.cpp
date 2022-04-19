#include<iostream>
using namespace std;
template <class T>
class matrix{
	T **p;
	T row,col;
	public:
	matrix(){}
	matrix(T d1,T d2){
		row=d1;
		col=d2;
		p=new int *[row];
		for(int i=0;i<row;i++){
			p[i]=new int [col];
		}
	}
	void get_element(void){
		cout<<"Enter the elements of the matrix : "<<endl; 
		for(int i=0;i<row;i++){
			for(int j=0;j<col;j++){
				cin>>p[i][j];
			}
		}
	}
	void display(void){
		for(int i=0;i<row;i++){
			for(int j=0;j<col;j++){
				cout<<p[i][j]<<" ";
			}
			cout<<endl;
		}
	}
	 matrix operator ++(int b);
	matrix operator --(int b);
	 matrix operator ++();
	matrix operator -- ();
};
template <class T>
	matrix<T> matrix<T>::operator ++(int b){
	matrix<T> temp(row,col);
	b=1;
	for(int i=0;i<temp.row;i++){
		for(int j=0;j<temp.col;j++){
			temp.p[i][j]=p[i][j]++;
		}
	}
	return temp;
}
template <class T>
	matrix<T> matrix<T>::operator --(int b){
	matrix<T> temp(row,col);
	b=1;
	for(int i=0;i<temp.row;i++){
		for(int j=0;j<temp.col;j++){
			temp.p[i][j]=p[i][j]--;
		}
	}
	return temp;
}
template <class T>
matrix<T> matrix<T>::operator ++(){
	matrix<T> temp(row,col);
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			temp.p[i][j]=++p[i][j];
		}
	}
	return temp;
}
template <class T>
matrix<T> matrix<T>::operator --(){
	matrix<T> temp(row,col);
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			temp.p[i][j]=--p[i][j];
		}
	}
	return temp;
}
int main(){
	int a,b;
	cout<<"Enter the dimensions of the martrix"<<endl;
	cin>>a>>b;
	matrix <int>m1(a,b);
	matrix <int>m2(a,b);
	m1.get_element();
	cout<<endl;
	cout<<"m1 before = "<<endl;
	m1.display();
	cout<<endl;
	
	m2=m1--;
	cout<<"After post-decrement : "<<endl;
	cout<<"m1 = "<<endl;
	m1.display();
	cout<<"m2 = "<<endl;
	m2.display();
	
	
	m2=m1++;
	cout<<"After post-increment : "<<endl;
	cout<<"m1 = "<<endl;
	m1.display();
	cout<<"m2 = "<<endl;
	m2.display();
	
	m2=--m1;
	cout<<"After pre-decrement : "<<endl;
	cout<<"m1 = "<<endl;
	m1.display();
	cout<<"m2 = "<<endl;
	m2.display();
	
	m2=++m1;
	cout<<"After pre-increment : "<<endl;
	cout<<"m1 = "<<endl;
	m1.display();
	cout<<"m2 = "<<endl;
	m2.display();
	return 0;
}
