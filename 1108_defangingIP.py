class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = list(address)

        for i in range(len(address)):
            if address[i] == '.':
                address[i] = '[.]'
        return ''.join(address)
