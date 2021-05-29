import React, { useEffect, useState } from "react";
import Lottie from "react-lottie";


import * as location from "../../Assets/loader_lottie.json";
import Main from '../../Main/Main'





const defaultOptions1 = {
  loop: true,
  autoplay: true,
  animationData: location.default,
  rendererSettings: {
    preserveAspectRatio: "xMidYMid slice",
  },
};

const defaultOptions2 = {
    loop: true,
    autoplay: true,
    animationData: location.default,
    rendererSettings: {
      preserveAspectRatio: "xMidYMid slice",
    },
  };


export function Preloader() {
    
    const [loading, setloading] = useState(undefined);
    const [completed, setcompleted] = useState(undefined);
  
    useEffect(() => {
      setTimeout(() => {
        fetch("https://jsonplaceholder.typicode.com/posts")
          .then((response) => response.json())
          .then((json) => {
            console.log(json);
            
            setloading(true);
  
            setTimeout(() => {
              setcompleted(true);
            }, 1000);
          });
      }, 2000);
    }, []);
  
    return (
      <div>
        {!completed ? (
          <div className="preloader">
            {!loading ? (
              <Lottie options={defaultOptions1} height={300} width={300} />
            ) : (
              <Lottie options={defaultOptions2} height={300} width={300} />
            )}
            
          </div>
        ) : (
          <div>
          <Main/>                   
          </div>
        )}
      </div>
    );
  }
  
export default Preloader;