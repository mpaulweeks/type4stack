function init_cardlist() {
			
	function getCardUrl(cardname) {
		return 'http://magiccards.info/query?q=' + cardname;
	}

	function getCardImageUrl(card_id) {
		return 'http://gatherer.wizards.com/Handlers/Image.ashx?type=card&multiverseid=' + card_id;
	}
	
	function getImage(card_id) {
		return '<img class="cardimage" '
			+ 'alt="' + card_id + '" '
			+ 'src="'
			+ getCardImageUrl(card_id)
			+ '"><img/>';
	}

	function getCardDiv(showArt, card) {
		var data = card.split(":");
		var cardname = data[0];
		var card_id = data[1];
		if(showArt) {
			return '<a href="'
				+ getCardUrl(cardname)
				+ '" target="_blank">'
				+ getImage(card_id)
				+ '</a>';
		} else {		
			return '<div><a href="'
				+ getCardUrl(cardname)
				+ '" class="mtgcard" target="_blank">'
				+ cardname
				+ '</a></div>';
		}
	}

	function toggle(elm){
		var $this = elm;
		$this.find('.cardlistdisplay').remove();
		
		var cards = $this.find('.data').html().split('|');
		var showArt = $this.data('art');
		$this.data('art', !showArt);
	
		var html = '';
		for (i = 0; i < cards.length; i++) {
			var card = cards[i].trim();
			html += getCardDiv(showArt, card);
		}
		if (showArt) {
			html = '<div class="cardlistdisplay">'
				+ html 
				+ '</div>';
		} else {
			html = '<div class="cardlistdisplay columned">'
				+ html
				+ '</div>';
		}		
		$this.append(html);
		init_autocard();
	}

	$('.cardlist').each(function () {
		var $this = $(this);
		$this.find('.toggle').on('click', function (){
			toggle($this);
		});
		toggle($this); //run now for init
	});
}