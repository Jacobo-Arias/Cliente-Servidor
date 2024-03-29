/*
Paralelismo local calculando celda por celda de una matriz con hilos
*/
#include <iostream>
#include <vector>
#include <chrono>

#include "Threadpool.hh"

using namespace std;
const int n = 3;

int multiplicacion(const int fil[n], const int col[n]){
    int result = 0;
    for(int i=0;i<n;i++){
        result += fil[i]*col[i];
    }
    return result;
}


int main()
{
    int A[n][n] = {{1,2,3},  //  1 2 3     1 2 3     6 12 18
                   {2,3,4},  //  2 3 4  X  1 2 3  =  9 18 27
                   {3,4,5}}; //  3 4 5     1 2 3    12 24 36

    int B[n][n] = {{1,2,3},
                   {1,2,3},
                   {1,2,3}};

    ThreadPool pool(thread::hardware_concurrency());
    vector< future<int> > results;
    auto start = chrono::system_clock::now();
    for(int i = 0; i < n;i++){
        for(int j = 0;j<n;j++){
            results.emplace_back(
                pool.enqueue([A,B,i,j] {
                    int resultado = 0;
                    for(int k=0;k<n;k++)
                        resultado += A[i][k]*B[k][j];
                    return resultado;
                })
            );
        }
    }
    int matrizresult[n][n];
    int i = 0,j = 0;
    for(auto && result: results){
        int resultados = result.get();
        matrizresult[i][j] = resultados;
        j++;
        if (j == n){
            j = 0;
            i++;
        }
    }
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++)
            cout<<matrizresult[i][j]<<" | ";
        cout<<endl;
    }
    auto end = chrono::system_clock::now();
    chrono::duration<float,milli> duration = end - start;
    cout <<endl<<"Para una multiplicación de dos matrices de "<<n<<" por "<<n<<"\nSe dardó: "<< duration.count() << "milisegundos" << endl;
    return 0;
}
