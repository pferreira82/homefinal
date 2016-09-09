(function(){

	var settings = {
		channel0: 'pi-house-temp',
		channel1: 'pi-house',
		publish_key: '',
		subscribe_key: ''
	};

	var pubnub = PUBNUB(settings);

	var door = document.getElementById('door');
	var lightLiving = document.getElementById('lightliving');
	var fan = document.getElementById('fan');
	var fireplace = document.getElementById('fireplace');

	pubnub.subscribe({
		channel: settings.channel0,
		callback: function(m) {
			if(m.temperature) {
				document.querySelector('[data-temperature]').dataset.temperature = m.temperature;
			}
			if(m.humidity) {
				document.querySelector('[data-humidity]').dataset.humidity = m.humidity;
			}
		}
	})

	/* 
		Data settings:

		Servo

		item: 'door'
		open: true | false

		LED

		item: 'light-*'
		brightness: 0 - 10

	*/

	function publishUpdate(data) {
		pubnub.publish({
			channel: settings.channel1, 
			message: data
		});
	}

	// UI EVENTS
	door.addEventListener('change', function(e){
		publishUpdate({item: 'door', open: +this.checked});
	}, false);

	lightLiving.addEventListener('change', function(e){
		publishUpdate({item: 'lightliving', on: +this.checked});
	}, false);

	fan.addEventListener('change', function(e){
		publishUpdate({item: 'fan', on: +this.checked});
	}, false);

	fireplace.addEventListener('change', function(e){
		publishUpdate({item: 'fireplace', brightness: +this.value});
	}, false);



})();
