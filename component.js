/**
* This React class is intended to query an endpoint that will return an alphanumeric string, after clicking a button.
* This component is passed a prop "apiQueryDelay", which delays the endpoint request by N milliseconds. There is a 
* second button to disable this functionality and have the endpoint request run immediately after button click.
* This data is then to be displayed inside a simple container.
* The "queryAPI" XHR handler will return the endpoint response in the form of a Promise (such as axios, fetch).
* The response object will look like the following: {data: "A0B3HCJ"}
* The containing element ref isn't used, but should remain within the class.
* Please identify, correct and comment on any errors or bad practices you see in the React component class below.
* Additionally, please feel free to change the code style as you see fit.
* Please note - React version for this exercise is 15.5.4
*/

import React, {Component} from 'react'; // Component import needs to be enclosed within curly braces
import queryAPI from 'queryAPI';


export class ShowResultsFromAPI extends Component() {
  constructor(props) { // constructor needs to take in props
    super(props);
    this.state = {
      container : null,
      data : '',
      error: false
    };
    // container should be placed in the component's state
    // data and error state properties also need to be added to the state
  }

  // I have converted the onDisableDelay method to an arrow function type method
  onDisableDelay = () => {
    this.props.apiQueryDelay = 0;
  }

  // I have converted the click method to an arrow function type method
  click = () => {
    if (this.props.apiQueryDelay) {
      setTimeout(function() {
        this.fetchData();
      }, this.props.apiQueryDelay);
    }
  }

  fetchData() {
    queryAPI()
      .then(function(response) {
        if (response.data) {
          this.setState({
            data: response.data
          });
          // since i have set the initial value for error in state to false, we dont't need to reset it here
        }
      });
  }

  render() {
    // I have destructured data and error properties from the component's state
    const { data, error } = this.state
    /**
     * Changes in the return method
     * - I changed the conditional if to an inline conditional statement since we are using it with in the return of the render method
     * - I replaced the statically typed data text with actual data coming from our state
     * - Because the onDisableDelay and click methods were converted to arrow functions, we don't have to bind them to this component class
     * - I also changed the button elements to lower case
     * - All html tags have been enclosed in fragment tags
     */

    return (
      <>
        <div class="content-container" ref="container">
            {error?
              <p>Sorry - there was an error with your request.</p>:
            <p>{data}</p>}
          </div>
        <button onClick={this.onDisableDelay}>Disable request delay</button>
        <button onClick={this.click}>Request data from endpoint</button>
      </>
    )
  }
}

ShowResultsFromAPI.displayName = {
  name: "ShowResultsFromAPI"
};
ShowResultsFromAPI.defaultProps = {
  apiQueryDelay: 0
};
ShowResultsFromAPI.propTypes = {
  apiQueryDelay: React.propTypes.number
};
