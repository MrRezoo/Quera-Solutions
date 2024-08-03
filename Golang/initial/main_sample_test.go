package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSample(t *testing.T) {
	str := HelloCodeCup(6)
	assert.Equal(t, "Hello CodeCup 6", str)
}
