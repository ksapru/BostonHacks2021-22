import './App.css'; 
import Navbar from './components/Navbar';
import Webcam from 'react-webcam';

function App() {


  return ( 
    
      <div className="App">      
      <Navbar></Navbar>
  <header className="App-header">
    <Webcam
  
      style={{
        position: "absolute",
        marginLeft: "auto",
        marginRight: "auto",
        left: 0,
        right: 0,
        textAlign: "center",
        zindex: 9,
        width: 640,
        height: 480,
      }}
    />
    <canvas
 
      style={{
        position: "absolute",
        marginLeft: "auto",
        marginRight: "auto",
        left: 0,
        right: 0,
        textAlign: "center",
        zindex: 9,
        width: 640,
        height: 480,
      }}
    />
    </header>
 

    </div>
    );
  }

export default App;