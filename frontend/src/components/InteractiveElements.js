import React from 'react';

const InteractiveElements = ({ elements }) => {
  if (!elements || !Array.isArray(elements) || elements.length === 0) {
    return null;
  }

  const renderElement = (element, index) => {
    switch (element.type) {
      case 'quiz':
        return (
          <div key={index} className="interactive-quiz">
            <h4>{element.question}</h4>
            <ul>
              {element.options.map((option, optIndex) => (
                <li key={optIndex}>
                  <label>
                    <input 
                      type="radio" 
                      name={`quiz-${index}`} 
                      value={option}
                    />
                    {option}
                  </label>
                </li>
              ))}
            </ul>
          </div>
        );
      case 'simulation':
        return (
          <div key={index} className="interactive-simulation">
            <h4>{element.title}</h4>
            <div className="simulation-container">
              <p>Simulation: {element.description}</p>
              {/* Add simulation component based on element configuration */}
            </div>
          </div>
        );
      case 'code-sandbox':
        return (
          <div key={index} className="interactive-code-sandbox">
            <h4>{element.title}</h4>
            <div className="code-sandbox-container">
              <p>Code Sandbox: {element.description}</p>
              {/* Add code editor component */}
            </div>
          </div>
        );
      default:
        return null;
    }
  };

  return (
    <div className="interactive-elements-container">
      {elements.map((element, index) => renderElement(element, index))}
    </div>
  );
};

export default InteractiveElements;