/*
Paralelismo local calculando fila por fila de una matriz con hilos
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

    // cout <<thread::hardware_concurrency() << endl;
    ThreadPool pool(thread::hardware_concurrency());
    vector< future<int> > results;
    for(int i = 0; i < n;i++){
            // cout<<i<<j<<endl;
            results.emplace_back(
                pool.enqueue([A,B,i] {
                    int resultado[n];
                    for(int j = 0;j<n;j++){
                        resultado[j]=0;
                        for(int k=0;k<n;k++)
                            resultado[j] += A[i][k]*B[k][j];
                    }
                    return resultado;
                })
            );
    }
    int matrizresult[n][n];
    int i = 0,j = 0;
    for(auto && result: results){
        int resultados = result.get();
        cout << resultados << ' ';
        // matrizresult[i][j] = resultados;
        // j++;
        // if (j == n){
        //     j = 0;
        //     i++;
        // }
    }
    cout <<"hemos terminado"<< endl;
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++)
            cout<<matrizresult[i][j]<<" | ";
        cout<<endl;
    }
    return 0;
}
