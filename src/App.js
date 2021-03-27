import useSunCircum from './useSunCircum';

const App = () => {
  const [pi, sunCircum, getPi] = useSunCircum();

  return (
      <div className="ui segment" style={{width: "50%", wordWrap: 'break-word', margin: '20px'}}>
        <h4 class="ui header">Pi: </h4>
        <p>{pi}</p>

        <h4 class="ui header">Sun circumference: </h4>
        <p>{sunCircum} km</p>

        <button className="ui olive button" onClick={() => getPi()} style={{margin: '20px'}}>
            Update PI
        </button>
      </div>
  );
}

export default App;
