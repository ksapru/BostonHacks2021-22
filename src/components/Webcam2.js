import logo from './logo.svg';
import './App.css';
import Webcam from "react-webcam";


function Webcam2() {


return (
  <div className="App">
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

export default Webcam2;