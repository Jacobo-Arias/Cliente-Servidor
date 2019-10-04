#include <iostream>
#include <zmqpp/zmqpp.hpp>
#include <string>
#include <chrono>
#include <thread>

using namespace std;
using namespace zmqpp;

int main() {
  context ctx;
  socket work(ctx, socket_type::pull);
  work.connect("tcp://localhost:5557");

  socket sink(ctx, socket_type::push);
  sink.connect("tcp://localhost:5558");

  while(true) {
    message s;
    work.receive(s);

    string text;
    s >> text;
    cout << "Work received " << text << endl;

    int tsleep = stoi(text);
    this_thread::sleep_for(chrono::milliseconds(tsleep));

    message rep;
    rep << "hi!";
    sink.send(rep);
  }


  cout << "Hello from C++ folks" << endl;
  return 0;
}
